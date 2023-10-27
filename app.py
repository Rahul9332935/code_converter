from flask import Flask, render_template, request, jsonify
import openaiData
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api/codeConverter", methods=["POST"])
def code_convertor():
    codeobj = request.get_json()
    code = codeobj.get('code')
    lang = codeobj.get('lang')
    data = openaiData.code_converter(code, lang)
    return jsonify(text=data)

@app.route("/api/codeDebugger", methods=["POST"])
def code_debugger():
    codeobj = request.get_json()
    code = codeobj.get('code')
    data = openaiData.codeDebuger(code)
    return jsonify(text=data)

@app.route("/api/codeQualityChecker", methods=["POST"])
def code_quality_checker():
    codeobj = request.get_json()
    code = codeobj.get('code')
    data = openaiData.code_quality_checker(code)
    return jsonify(text=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
