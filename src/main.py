import os
from read_csv import read_csv
from plot import plot
from regularize import regularize_curves
from symmetry import find_symmetry
from complete import complete_curves
from rasterization import polylines2svg

def process_file(file_path, output_dir):
    # Load and visualize initial curves
    path_XYs = read_csv(file_path)
    
    # Regularize curves
    regularized_curves = regularize_curves(path_XYs)
    
    # Find symmetries in curves
    symmetric_curves = find_symmetry(regularized_curves)
    
    # Complete incomplete curves
    completed_curves = complete_curves(symmetric_curves)
    
    # Determine output file names
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    svg_filename = f"{base_filename}_sol.svg"
    svg_path = os.path.join(output_dir, svg_filename)
    
    # Rasterize and save the completed curves as SVG
    polylines2svg(completed_curves, svg_path)
    
    print(f"SVG file saved: {svg_path}")
    # Optionally save the modified data as CSV if required
    # e.g., save_csv(completed_curves, os.path.join(output_dir, f"{base_filename}_completed.csv"))

def main():
    # Get the absolute path to the data directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    output_dir = os.path.join(base_dir, 'data')

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each CSV file in the data directory
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.csv') and not file_name.endswith('_sol.csv'):
            file_path = os.path.join(data_dir, file_name)
            process_file(file_path, output_dir)

if __name__ == '__main__':
    main()
