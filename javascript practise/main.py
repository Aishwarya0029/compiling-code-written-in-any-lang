from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for storing expected output hashes
questions = {
    "Solidity": {
        "Easy": {"code": "contract HelloWorld { function sayHello() public pure returns(string memory) { return 'Hello, World!'; } }", "hash": "c1f5e1a7"},
        "Medium": {"code": "", "hash": ""},
        "Hard": {"code": "", "hash": ""}
    },
    "Rust": {
        "Easy": {"code": "", "hash": ""},
        "Medium": {"code": "", "hash": ""},
        "Hard": {"code": "", "hash": ""}
    },
    "Motoko": {
        "Easy": {"code": "", "hash": ""},
        "Medium": {"code": "", "hash": ""},
        "Hard": {"code": "", "hash": ""}
    }
}
