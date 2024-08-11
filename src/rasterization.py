import cairosvg
import numpy as np
import svgwrite

def polylines2svg(paths_XYs, svg_path):
    W, H = 0, 0
    
    # Calculate the dimensions based on the paths
    for path_XYs in paths_XYs:
        for XY in path_XYs:
            W = max(W, np.max(XY[:, 0]))
            H = max(H, np.max(XY[:, 1]))
            
    padding = 0.1
    W, H = int(W + padding * W), int(H + padding * H)
    
    # Create a new SVG drawing
    dwg = svgwrite.Drawing(svg_path, profile='tiny', shape_rendering='crispEdges')
    group = dwg.g()

    # Define line styles
    colours = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']  # Example colors

    for i, path in enumerate(paths_XYs):
        path_data = []
        c = colours[i % len(colours)]
        
        for XY in path:
            path_data.append(("M", (XY[0, 0], XY[0, 1])))
            for j in range(1, len(XY)):
                path_data.append(("L", (XY[j, 0], XY[j, 1])))
            
            if np.allclose(XY[0], XY[-1]):
                path_data.append(("Z", None))
                
            group.add(dwg.path(d=path_data, fill='none', stroke=c, stroke_width=2))

    dwg.add(group)
    dwg.save()

    png_path = svg_path.replace('.svg', '.png')
    fact = max(1, 1024 // min(H, W))
    
    cairosvg.svg2png(
        url=svg_path, 
        write_to=png_path,
        parent_width=W, 
        parent_height=H,
        output_width=fact * W, 
        output_height=fact * H,
        background_color='white'
    )