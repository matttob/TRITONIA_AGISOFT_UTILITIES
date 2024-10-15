import Metashape

def calculate_selected_area():
    # Check if the document is open
    doc = Metashape.app.document
    if not len(doc.chunks):
        print("No chunk loaded")
        return
    
    chunk = doc.chunk

    # Check if the chunk has a model
    if not chunk.model:
        print("No 3D model found")
        return

    # Check if any selection is made
    selected_faces = [face for face in chunk.model.faces if face.selected]
    if not selected_faces:
        print("No faces selected.")
        return

    # Get the transformation matrix (to convert vertices to real-world coordinates)
    T = chunk.transform.matrix

    # Calculate the surface area
    total_area = 0.0
    for face in selected_faces:
        # Extract the vertices of the face and transform them to real-world coordinates
        vertices = [transform_vertex(chunk.model.vertices[v_id].coord, T) for v_id in face.vertices]
        
        # Calculate the area of the face
        area = calculate_face_area(vertices)
        total_area += area

    # Output the result
    print(f"Total Selected Surface Area: {total_area:.6f} square meters")
    
def transform_vertex(vertex, T):
    # Convert the vertex to a 4D homogeneous vector (x, y, z, 1.0)
    v = Metashape.Vector([vertex.x, vertex.y, vertex.z, 1.0])
    
    # Multiply the transformation matrix T by the 4D vector v
    v_transformed = T * v
    
    # Return the transformed vertex as a 3D point (ignore the homogeneous coordinate)
    return Metashape.Vector([v_transformed.x, v_transformed.y, v_transformed.z])

def calculate_face_area(vertices):
    # Assuming vertices contains 3 points (triangular face), 
    # We calculate the cross-product manually to get the area of the triangle
    
    v0 = vertices[0]
    v1 = vertices[1]
    v2 = vertices[2]

    # Calculate vectors from v0 to v1 and v0 to v2
    vec1 = v1 - v0
    vec2 = v2 - v0

    # Manually compute the cross-product
    cross_x = vec1.y * vec2.z - vec1.z * vec2.y
    cross_y = vec1.z * vec2.x - vec1.x * vec2.z
    cross_z = vec1.x * vec2.y - vec1.y * vec2.x

    # Compute the magnitude of the cross-product vector (norm)
    cross_product_norm = (cross_x**2 + cross_y**2 + cross_z**2)**0.5

    # The area of the triangle is half the magnitude of the cross-product
    area = 0.5 * cross_product_norm

    return area

# Add the function as a menu item
Metashape.app.addMenuItem("Custom/Calculate Selected Area", calculate_selected_area)
print("Plugin loaded. Go to Custom -> Calculate Selected Area to use.")
