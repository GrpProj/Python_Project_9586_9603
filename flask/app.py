from flask import Flask,redirect,url_for,render_template,request, send_file,jsonify
from bin.filters import apply_filter

app=Flask(__name__)
filters_available = [
    "blur",
    "contour",
    "edge_enhance",
    "edge_enhance_more",
    "emboss",
    "find_edges",
    "sharpen",
    "smooth",
    "smooth_more"
]

@app.route('/',methods=['GET','POST'])
def index():
    response = {
        "filters_available": filters_available,
        "usage":{"http_method":"POST","URL": "/<filters_available>/"},   
    }
    return jsonify(response)
    """
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')
    """
    

@app.post("/<filter>")
def image_filter(filter):
    if filter not in filters_available:
        response = {"error":"incorrect filter"}
        return jsonify(response)
    file = request.files["image"]
    if not file:
        response = {"error":"no file present"}
        return(response)
    
    filtered_image = apply_filter(file, filter)
    
    return send_file(filtered_image, mimetype="image/JPEG")
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)