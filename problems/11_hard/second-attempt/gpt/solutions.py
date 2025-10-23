"""
Five robust implementations (func1..func5) to compute the tight rectangular
polygonal outline of a list of rectangles.

Rectangles format:
{ "x": int, "y": int, "width": int, "height": int }
Origin is top-left (y increases downward).

Outputs: list of points [{ "x":..., "y":... }, ...] describing the polygonal
boundary in vertex order (no repeated closing vertex). For degenerate cases
(e.g., all rectangles are the same point), returns that point.
"""

from collections import defaultdict, deque
from itertools import product


def _normalize_rects(rects):
    """
    Return deduplicated list and collect degenerate points/lines specially.
    Each rectangle normalized to (x1,y1,x2,y2) where x2 = x1 + width, y2 = y1 + height.
    """
    normalized = []
    seen = set()
    for r in rects:
        x1 = int(r["x"])
        y1 = int(r["y"])
        x2 = x1 + int(r.get("width", 0))
        y2 = y1 + int(r.get("height", 0))
        tup = (x1, y1, x2, y2)
        if tup in seen:
            continue
        seen.add(tup)
        normalized.append(tup)
    return normalized


def _edge_key(a, b):
    """Canonical undirected key for an edge between points a and b."""
    return (a, b) if a <= b else (b, a)


def _collect_edges_from_rect(x1, y1, x2, y2):
    """
    Collect edges for a rectangle defined by corners (x1,y1) top-left and (x2,y2)
    bottom-right. Handles degenerate rectangles:
      - If x1==x2 and y1==y2 -> no edges (a point)
      - If x1==x2 or y1==y2 -> produces a single segment (line)
    Edges are returned as directed tuples (p, q) where p=(x,y), q=(x,y).
    """
    edges = []
    if x1 == x2 and y1 == y2:
        # point -> no edges
        return edges
    if x1 == x2:
        # vertical line from (x1,y1) -> (x1,y2)
        if y1 < y2:
            edges.append(((x1, y1), (x2, y2)))
        else:
            edges.append(((x2, y2), (x1, y1)))
        return edges
    if y1 == y2:
        # horizontal line
        if x1 < x2:
            edges.append(((x1, y1), (x2, y2)))
        else:
            edges.append(((x2, y2), (x1, y1)))
        return edges
    # normal rectangle (positive area) - add four directed edges (clockwise)
    top = ((x1, y1), (x2, y1))
    right = ((x2, y1), (x2, y2))
    bottom = ((x2, y2), (x1, y2))
    left = ((x1, y2), (x1, y1))
    edges.extend([top, right, bottom, left])
    return edges


def _assemble_polygon_from_boundary_edges(boundary_edges):
    """
    Given a list of undirected boundary edges (each edge as (p,q) without direction,
    where p and q are 2-tuples), assemble an ordered polygonal path.
    If multiple disjoint loops exist, we will return the outer loop that
    starts with the top-leftmost vertex (min y, then min x). For purely
    degenerate single-point cases, returns that point.
    """
    if not boundary_edges:
        return []

    # Build adjacency
    adj = defaultdict(list)
    vertices = set()
    for a, b in boundary_edges:
        adj[a].append(b)
        adj[b].append(a)
        vertices.add(a)
        vertices.add(b)

    # If only one vertex (shouldn't normally happen with edges) handle safely:
    if len(vertices) == 1:
        v = next(iter(vertices))
        return [v]

    # Find starting vertex: smallest y (top), tie-breaker smallest x (left)
    start = min(vertices, key=lambda p: (p[1], p[0]))

    # Walk a loop: since boundary of union of axis-aligned rectangles produces
    # vertices of degree 2 on simple loops, this greedy walk will follow the loop.
    path = [start]
    current = start
    prev = None
    while True:
        neighbors = adj[current]
        # choose neighbor not equal to prev; if both equal or only one neighbor, take it
        next_v = None
        if len(neighbors) == 0:
            break
        elif len(neighbors) == 1:
            next_v = neighbors[0]
        else:
            # pick neighbor != prev; if prev is None choose the neighbor with
            # smallest polar ordering (prefer right/down as typical for top-left start)
            if prev is None:
                # order neighbors by (dx, dy) from current, prefer right, then down, then left, then up
                def order(n):
                    dx = n[0] - current[0]
                    dy = n[1] - current[1]
                    # assign quadrants to create consistent tie breaking: right/down preferred
                    return (abs(dy), abs(dx), dx, dy)
                next_v = min(neighbors, key=order)
            else:
                # pick the neighbor that is not prev
                if neighbors[0] == prev:
                    next_v = neighbors[1]
                elif neighbors[1] == prev:
                    next_v = neighbors[0]
                else:
                    # fallback: pick first
                    next_v = neighbors[0]
        if next_v is None:
            break
        if next_v == start:
            # closed loop complete
            break
        if next_v in path:
            # we've hit a previously visited vertex that's not the start: stop to avoid infinite loops
            break
        path.append(next_v)
        prev, current = current, next_v

    return path


# -------------------------
# func1: robust edge-count + assemble (canonical)
# -------------------------
def func1(rects):
    rects_n = _normalize_rects(rects)
    if not rects_n:
        return []
    # Collect edges and count undirected occurrences
    undirected_count = defaultdict(int)
    directed_examples = defaultdict(list)
    points_only = set()
    for x1, y1, x2, y2 in rects_n:
        if x1 == x2 and y1 == y2:
            points_only.add((x1, y1))
            continue
        edges = _collect_edges_from_rect(x1, y1, x2, y2)
        for p, q in edges:
            key = _edge_key(p, q)
            undirected_count[key] += 1
            directed_examples[key].append((p, q))
    # If we only have points (all rects were the same points), return deduped points
    if not undirected_count and points_only:
        return [{"x": x, "y": y} for x, y in sorted(points_only, key=lambda p: (p[1], p[0]))]

    # Keep edges that appear odd number of times -> boundary edges (1 for typical union)
    boundary_undirected = [edge for edge, c in undirected_count.items() if c % 2 == 1]
    path_vertices = _assemble_polygon_from_boundary_edges(boundary_undirected)
    return [{"x": x, "y": y} for x, y in path_vertices]


# -------------------------
# func2: rasterization (pixel union) + contour trace (Moore-like)
# Good for small coordinates; handles single-point case.
# -------------------------
def func2(rects):
    rects_n = _normalize_rects(rects)
    if not rects_n:
        return []
    cells = set()
    points_only = set()
    # We'll treat each integer unit cell [x, x+1) x [y, y+1) as filled when width/height > 0.
    for x1, y1, x2, y2 in rects_n:
        if x1 == x2 and y1 == y2:
            points_only.add((x1, y1))
            continue
        # If either dimension is zero, we mark the integer coordinates along the line
        if x1 == x2:
            # vertical line from y1 to y2
            ys = range(min(y1, y2), max(y1, y2) + 1)
            for y in ys:
                cells.add((x1, y))
            continue
        if y1 == y2:
            xs = range(min(x1, x2), max(x1, x2) + 1)
            for x in xs:
                cells.add((x, y1))
            continue
        for x in range(min(x1, x2), max(x1, x2)):
            for y in range(min(y1, y2), max(y1, y2)):
                cells.add((x, y))
    if not cells:
        # only points/lines present
        if points_only:
            return [{"x": x, "y": y} for x, y in sorted(points_only, key=lambda p: (p[1], p[0]))]
        return []

    # Find boundary edges of occupied unit cells
    edges = set()
    for (x, y) in cells:
        # each unit cell has four edges; if neighbor missing, that edge belongs to boundary
        if (x, y - 1) not in cells:
            edges.add(((x, y), (x + 1, y)))
        if (x + 1, y) not in cells:
            edges.add(((x + 1, y), (x + 1, y + 1)))
        if (x, y + 1) not in cells:
            edges.add(((x, y + 1), (x + 1, y + 1)))
        if (x - 1, y) not in cells:
            edges.add(((x, y), (x, y + 1)))
    # Convert undirected edge set to list of tuples (a,b) with consistent ordering
    undirected = [ (a,b) if a<=b else (b,a) for (a,b) in edges ]
    # assemble polygon
    path = _assemble_polygon_from_boundary_edges(undirected)
    return [{"x": x, "y": y} for x, y in path]


# -------------------------
# func3: shapely-based union if available (most robust & compact).
# Falls back to func1 if shapely missing.
# -------------------------
def func3(rects):
    try:
        from shapely.geometry import Polygon, Point, LineString
        from shapely.ops import unary_union
    except Exception:
        # shapely missing: fall back to func1
        return func1(rects)

    rects_n = _normalize_rects(rects)
    if not rects_n:
        return []

    geoms = []
    points_only = []
    for x1, y1, x2, y2 in rects_n:
        if x1 == x2 and y1 == y2:
            points_only.append(Point(x1, y1))
            continue
        if x1 == x2 or y1 == y2:
            # line
            geoms.append(LineString([(x1, y1), (x2, y2)]))
            continue
        geoms.append(Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]))

    if not geoms:
        # only points
        if points_only:
            uniq = sorted({(int(p.x), int(p.y)) for p in points_only}, key=lambda p: (p[1], p[0]))
            return [{"x": x, "y": y} for x, y in uniq]
        return []

    union = unary_union(geoms)
    # union could be Polygon, MultiPolygon, LineString, Point, etc.
    if union.is_empty:
        return []
    # prefer polygon exterior; if line or point, handle separately
    if union.geom_type == "Polygon":
        coords = list(union.exterior.coords)[:-1]
        return [{"x": int(round(cx)), "y": int(round(cy))} for (cx, cy) in coords]
    elif union.geom_type == "MultiPolygon":
        # pick the largest polygon by area (outermost)
        largest = max(union.geoms, key=lambda g: g.area)
        coords = list(largest.exterior.coords)[:-1]
        return [{"x": int(round(cx)), "y": int(round(cy))} for (cx, cy) in coords]
    elif union.geom_type == "LineString":
        coords = list(union.coords)
        return [{"x": int(round(cx)), "y": int(round(cy))} for (cx, cy) in coords]
    elif union.geom_type == "Point":
        p = union
        return [{"x": int(round(p.x)), "y": int(round(p.y))}]
    else:
        # fallback
        return func1(rects)


# -------------------------
# func4: scanline union of horizontal intervals, then build outline
# -------------------------
def func4(rects):
    rects_n = _normalize_rects(rects)
    if not rects_n:
        return []

    # Build mapping from each integer y to list of [x_start, x_end) intervals (for positive-area rects)
    intervals_by_y = defaultdict(list)
    points_only = set()
    for x1, y1, x2, y2 in rects_n:
        if x1 == x2 and y1 == y2:
            points_only.add((x1, y1))
            continue
        # for degenerate horizontal/vertical lines treat specially: include small intervals
        if x1 == x2:
            # vertical line: mark intervals on each y between y1 and y2 inclusive
            for y in range(min(y1, y2), max(y1, y2)+1):
                intervals_by_y[y].append((x1, x1+1))
            continue
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                intervals_by_y[y1].append((x, x+1))
            continue
        for y in range(min(y1, y2), max(y1, y2)):
            intervals_by_y[y].append((min(x1, x2), max(x1, x2)))

    if not intervals_by_y:
        if points_only:
            return [{"x": x, "y": y} for x, y in sorted(points_only, key=lambda p: (p[1], p[0]))]
        return []

    # Merge intervals each row
    merged_by_y = {}
    for y, ints in intervals_by_y.items():
        ints_sorted = sorted(ints)
        merged = []
        cur_s, cur_e = ints_sorted[0]
        for s, e in ints_sorted[1:]:
            if s <= cur_e:
                cur_e = max(cur_e, e)
            else:
                merged.append((cur_s, cur_e))
                cur_s, cur_e = s, e
        merged.append((cur_s, cur_e))
        merged_by_y[y] = merged

    # Now build vertical edges from differences between consecutive scanlines
    edges = set()
    ys = sorted(merged_by_y.keys())
    ymin, ymax = ys[0], ys[-1]
    # top edges: for first row, each merged interval contributes a top edge
    for s, e in merged_by_y[ymin]:
        edges.add(((s, ymin), (e, ymin)))
    # bottom edges: for last row, each merged interval contributes a bottom edge at y+1
    for s, e in merged_by_y[ymax]:
        edges.add(((s, ymax+1), (e, ymax+1)))
    # vertical transitions between rows
    for y in ys:
        next_y = y + 1
        cur = merged_by_y.get(y, [])
        nxt = merged_by_y.get(next_y, [])
        # intervals present in cur but not nxt -> bottom edges at next_y
        # intervals present in nxt but not cur -> top edges at next_y
        # compute differences by subtracting segments (use simple sweep)
        def subtract(a_list, b_list):
            res = []
            for a_s, a_e in a_list:
                s = a_s
                e = a_e
                for b_s, b_e in b_list:
                    if b_e <= s or b_s >= e:
                        continue
                    # overlap
                    if b_s <= s and b_e >= e:
                        s = e  # completely covered
                        break
                    if b_s <= s < b_e < e:
                        s = b_e
                    elif s < b_s < e <= b_e:
                        e = b_s
                    elif b_s > s and b_e < e:
                        # split
                        res.append((s, b_s))
                        s = b_e
                if s < e:
                    res.append((s, e))
            return res
        bottoms = subtract(cur, nxt)
        tops = subtract(nxt, cur)
        for s, e in bottoms:
            edges.add(((s, next_y), (e, next_y)))
        for s, e in tops:
            edges.add(((s, next_y), (e, next_y)))

    # Convert horizontal edges into undirected vertex edges (split edges into unit segments at integer coords)
    undirected_edges = set()
    for (a, b) in edges:
        (ax, ay), (bx, by) = a, b
        if ay == by:
            # horizontal, split into unit segments to create vertices
            sx, ex = min(ax, bx), max(ax, bx)
            for x in range(sx, ex):
                undirected_edges.add(((x, ay), (x+1, ay)))
        else:
            # vertical (unlikely here), split similarly
            sy, ey = min(ay, by), max(ay, by)
            for y in range(sy, ey):
                undirected_edges.add(((ax, y), (ax, y+1)))

    # assemble polygon
    undirected = [ (a,b) if a<=b else (b,a) for (a,b) in undirected_edges ]
    path = _assemble_polygon_from_boundary_edges(undirected)
    return [{"x": x, "y": y} for x, y in path]


# -------------------------
# func5: sweep-line merge rectangles into disjoint set then trace boundary
# This merges overlapping rects into maximal rectangles, then traces the union boundary.
# -------------------------
def func5(rects):
    rects_n = _normalize_rects(rects)
    if not rects_n:
        return []
    points_only = [ (x1,y1) for x1,y1,x2,y2 in rects_n if x1==x2 and y1==y2 ]
    rects_area = [ (x1,y1,x2,y2) for x1,y1,x2,y2 in rects_n if not (x1==x2 and y1==y2) ]
    if not rects_area:
        # only points
        if points_only:
            uniq = sorted(set(points_only), key=lambda p: (p[1], p[0]))
            return [{"x": x, "y": y} for x, y in uniq]
        return []

    # naive merging: repeatedly merge any two rectangles that overlap or touch into bounding rectangle
    changed = True
    merged = rects_area[:]
    while changed:
        changed = False
        new = []
        used = [False] * len(merged)
        for i in range(len(merged)):
            if used[i]:
                continue
            a = merged[i]
            ax1, ay1, ax2, ay2 = a
            merged_this = a
            used[i] = True
            for j in range(i+1, len(merged)):
                if used[j]:
                    continue
                bx1, by1, bx2, by2 = merged[j]
                # test overlap or adjacency (touching) in both axes
                if not (ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1):
                    # overlap or touch -> merge to bounding rect
                    nx1 = min(ax1, bx1)
                    ny1 = min(ay1, by1)
                    nx2 = max(ax2, bx2)
                    ny2 = max(ay2, by2)
                    merged_this = (nx1, ny1, nx2, ny2)
                    used[j] = True
                    changed = True
                    # update a with merged for further merges
                    ax1, ay1, ax2, ay2 = merged_this
            new.append(merged_this)
        merged = new

    # now produce edges for each merged rectangle
    undirected_edges = set()
    for x1, y1, x2, y2 in merged:
        e = _collect_edges_from_rect(x1, y1, x2, y2)
        for p, q in e:
            key = _edge_key(p, q)
            # count duplicates; if an edge appears twice among merged rects it's internal and should be removed.
            if key in undirected_edges:
                undirected_edges.remove(key)
            else:
                undirected_edges.add(key)
    # assemble polygon
    path = _assemble_polygon_from_boundary_edges(list(undirected_edges))
    return [{"x": x, "y": y} for x, y in path]


# -------------------------
# Small tests for the edge cases you asked about:
# -------------------------
if __name__ == "__main__":
    sample = [
        {"x": 2, "y": 2, "width": 5, "height": 4},
        {"x": 4, "y": 3, "width": 6, "height": 6},
        {"x": 8, "y": 1, "width": 5, "height": 4},
    ]

    print("=== sample union ===")
    for i, f in enumerate([func1, func2, func3, func4, func5], 1):
        try:
            out = f(sample)
            print(f"func{i} -> {out}")
        except Exception as e:
            print(f"func{i} error: {e}")

    print("\n=== three identical rectangles (non-degenerate) ===")
    rect = {"x": 1, "y": 1, "width": 3, "height": 2}
    three = [rect, rect, rect]
    for i, f in enumerate([func1, func2, func3, func4, func5], 1):
        try:
            out = f(three)
            print(f"func{i} -> {out}")
        except Exception as e:
            print(f"func{i} error: {e}")

    print("\n=== three identical points (degenerate) ===")
    pt = {"x": 5, "y": 5, "width": 0, "height": 0}
    three_pts = [pt, pt, pt]
    for i, f in enumerate([func1, func2, func3, func4, func5], 1):
        try:
            out = f(three_pts)
            print(f"func{i} -> {out}")
        except Exception as e:
            print(f"func{i} error: {e}")

funcs = [func1, func2, func3, func4, func5]