from flask import Flask,jsonify,request

employee = [
  {
    "id":"1",
    "name":"Sheetal gour",
    "age":"19"
  },
  {
    "id":"2",
    "name":"Akshat",
    "age":"21"
  }
]


app = Flask(__name__)

# Home page 
@app.route('/')
def get():
  return "Hello , Happy New Year"

# get details of all employee 
@app.route('/emp',methods=['GET'])
def get_emp():
  return jsonify({"employee":employee})

# get details of employee
@app.route('/emp/<name>',methods=['GET'])
def get_emp_with_name(name):
 
  for emp in employee:
    if emp['name'] == name:
      return jsonify({"emp":emp})

  return jsonify({"error":"Employee Not Found"})


# Add employee
@app.route('/emp/add',methods=['POST'])
def create_emp():
  req = request.get_json()
  new_emp = {
    "id":req['id'],
    "name":req['name'],
    "age":req['age']

  }
  employee.append(new_emp)
  return jsonify({"status":"Added"})
  

# Update employee details
@app.route('/emp/update/<name>',methods=['PUT'])
def update(name):

  for emp in employee:
    if emp['name'] == name:
      req = request.get_json()

      emp["name"] = req['name']
      emp["id"] = req['id']
      emp["age"] = req['age']

      return jsonify({'updated':emp})


    return jsonify({'error':"Employee not found"})


# delete employees
@app.route('/emp/delete/<name>',methods=['DELETE'])
def delete(name):

  for emp in employee:

    if emp['name'] == name:
      employee.remove(emp)
      return jsonify({"success":"Employee data deleted"})

  return jsonify({"error":"Doesn't exist"})



if __name__=="__main__":
    app.run(debug=True)