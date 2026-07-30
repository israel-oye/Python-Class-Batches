import 'dart:convert';

void main(){
  String jsonStr = '{"name": "Hammed Ilesanmi", "age": 35, "friends": ["Emmanuel Balogun", "Israel Kola"], "is_admin": false, "best_friend": null}';

  var object = jsonDecode(jsonStr);
  print(object['best_friend']);

  Map<String, dynamic> userData = {
    "name": "Kolawole Balogun",
    "date_of_birth": "2016-04-28T00:00",
    "contacts": ["Ajayi", "Bolanle", "Daramola"],
    "isVerified": false
  };

  print(jsonEncode(userData));
}