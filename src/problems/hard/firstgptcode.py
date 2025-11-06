# =====================================
# Problem: Polygonal outline of rectangles
# =====================================

from itertools import product

# ------------------------------------------------
# func1 — Simple grid fill + contour tracing
# ------------------------------------------------
def func1(rects):
    # Build filled pixel map
    points = set()
    for r in rects:
        for x in range(r["x"], r["x"] + r["width"]):
            for y in range(r["y"], r["y"] + r["height"]):
                points.add((x, y))
    # Find all "edges" of filled cells
    edges = set()
    for (x, y) in points:
        for dx, dy, direction in [(0, -1, "top"), (1, 0, "right"), (0, 1, "bottom"), (-1, 0, "left")]:
            if (x + dx, y + dy) not in points:
                if direction == "top":
                    edges.add(((x, y), (x + 1, y)))
                elif direction == "right":
                    edges.add(((x + 1, y), (x + 1, y + 1)))
                elif direction == "bottom":
                    edges.add(((x, y + 1), (x + 1, y + 1)))
                elif direction == "left":
                    edges.add(((x, y), (x, y + 1)))
    # Convert edges to path (simple sort by adjacency)
    if not edges:
        return []
    path = [min(edges)[0]]
    current = path[0]
    while edges:
        next_edges = [e for e in edges if e[0] == current or e[1] == current]
        if not next_edges:
            break
        e = next_edges[0]
        next_point = e[1] if e[0] == current else e[0]
        edges.remove(e)
        path.append(next_point)
        current = next_point
    return [{"x": x, "y": y} for x, y in path]


# ------------------------------------------------
# func2 — Use union of rectangle edges and detect boundary edges
# ------------------------------------------------
def func2(rects):
    edge_count = {}
    for r in rects:
        x1, y1 = r["x"], r["y"]
        x2, y2 = x1 + r["width"], y1 + r["height"]
        edges = [
            ((x1, y1), (x2, y1)),  # top
            ((x2, y1), (x2, y2)),  # right
            ((x2, y2), (x1, y2)),  # bottom
            ((x1, y2), (x1, y1)),  # left
        ]
        for e in edges:
            e_sorted = tuple(sorted(e))
            edge_count[e_sorted] = edge_count.get(e_sorted, 0) + 1
    # Keep only edges that appear once (outer boundary)
    boundary_edges = [e for e, c in edge_count.items() if c == 1]
    # Build path by adjacency
    if not boundary_edges:
        return []
    path = [boundary_edges[0][0]]
    edges = boundary_edges[:]
    current = path[0]
    while edges:
        next_edge = None
        for e in edges:
            if e[0] == current:
                next_edge = e
                current = e[1]
                break
            elif e[1] == current:
                next_edge = e
                current = e[0]
                break
        if not next_edge:
            break
        edges.remove(next_edge)
        path.append(current)
    return [{"x": x, "y": y} for x, y in path]


# ------------------------------------------------
# func3 — Merge horizontal/vertical spans after rasterizing outline
# ------------------------------------------------
def func3(rects):
    # Create a set of occupied pixels
    filled = set()
    for r in rects:
        for x, y in product(range(r["x"], r["x"] + r["width"]), range(r["y"], r["y"] + r["height"])):
            filled.add((x, y))
    # Get minimal x/y boundaries
    xs = [p[0] for p in filled]
    ys = [p[1] for p in filled]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    outline = []
    # Scan rows, detect edges
    for y in range(miny, maxy + 2):
        for x in range(minx, maxx + 2):
            if (x, y) in filled and (x - 1, y) not in filled:
                outline.append(((x - 1, y), (x, y)))
            if (x, y) in filled and (x, y - 1) not in filled:
                outline.append(((x, y - 1), (x, y)))
    # Sort points by adjacency
    points = []
    if outline:
        start = outline[0][0]
        current = start
        edges = outline[:]
        while edges:
            next_edge = next((e for e in edges if e[0] == current or e[1] == current), None)
            if not next_edge:
                break
            next_point = next_edge[1] if next_edge[0] == current else next_edge[0]
            points.append(next_point)
            edges.remove(next_edge)
            current = next_point
    return [{"x": x, "y": y} for x, y in points]


# ------------------------------------------------
# func4 — Geometric approach using shapely (if available)
# ------------------------------------------------
def func4(rects):
    try:
        from shapely.geometry import Polygon
        from shapely.ops import unary_union
    except ImportError:
        raise ImportError("Shapely is required for func4.")
    polys = []
    for r in rects:
        x, y, w, h = r["x"], r["y"], r["width"], r["height"]
        polys.append(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)]))
    union = unary_union(polys)
    exterior = list(union.exterior.coords)
    return [{"x": int(x), "y": int(y)} for x, y in exterior[:-1]]


# ------------------------------------------------
# func5 — Sweep-line merge of overlapping rectangles, then outline
# ------------------------------------------------
def func5(rects):
    # Compute merged min/max bounds in x
    rects_sorted = sorted(rects, key=lambda r: r["x"])
    merged = []
    for r in rects_sorted:
        if not merged:
            merged.append(r)
            continue
        last = merged[-1]
        if (r["x"] <= last["x"] + last["width"]) and (r["y"] < last["y"] + last["height"]) and (r["y"] + r["height"] > last["y"]):
            # merge horizontally overlapping
            nx = min(last["x"], r["x"])
            ny = min(last["y"], r["y"])
            nw = max(last["x"] + last["width"], r["x"] + r["width"]) - nx
            nh = max(last["y"] + last["height"], r["y"] + r["height"]) - ny
            merged[-1] = {"x": nx, "y": ny, "width": nw, "height": nh}
        else:
            merged.append(r)
    # Now outline the merged regions
    path = []
    for r in merged:
        x, y, w, h = r["x"], r["y"], r["width"], r["height"]
        path += [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    # Remove duplicates and order path
    unique = []
    for p in path:
        if p not in unique:
            unique.append(p)
    return [{"x": x, "y": y} for x, y in unique]


first_gpt = [func1, func2, func3, func4, func5]