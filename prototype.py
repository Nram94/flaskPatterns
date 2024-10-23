from flask import Flask, jsonify

app = Flask(__name__)

class UserProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clone(self):
        return UserProfile(self.name, self.age)

@app.route('/')
def clone_user():
    original_user = UserProfile("Alice", 25)
    cloned_user = original_user.clone()
    return jsonify(
        original_user={"name": original_user.name, "age": original_user.age},
        cloned_user={"name": cloned_user.name, "age": cloned_user.age}
    )

if __name__ == "__main__":
    app.run(debug=True)
