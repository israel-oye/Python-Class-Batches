import 'dart:convert';

void main(){
  String jsonStr = '{"classname": "Dev with Python", "students": 20, "is_completed": false, "reg_no": null}';
  var map = jsonDecode(jsonStr);
  print(map['is_completed']);
}