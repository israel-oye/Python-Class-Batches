let data = {
    name: "Emmanuel",
    height: 1.78,
    nationality: "Nigeria",
    hobby: null,
    friends: ["Hammed", "Bola", "Oyinkansola"]
};

// console.log(data["friends"]);
// console.log(typeof JSON.stringify(data));

let jsonString = '{"name": "Hammed Ilesanmi", "age": 35, "friends": ["Emmanuel Balogun", "Israel Kola"], "is_admin": false, "best_friend": null}';

let userData = JSON.parse(jsonString);
console.log(userData.friends[0]);
