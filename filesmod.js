const fs = require("node:fs/promises");

async function readFile() {
    try {
        const data = await fs.readFile("./file.txt", "utf-8");
        console.log(data);
    } catch(err) {
        console.log(err);
    }
}

readFile();

/*fs.readFile("./file.txt", "utf-8")
.then((data) => console.log(data))
.catch((error) => console.log(error));*/


/*const fs = require("node:fs");

const contents = fs.readFileSync("./file.txt", "utf-8");
console.log(contents);

fs.readFile("./file.txt", "utf-8", (error, data) => {
    if(error) {
        console.log(error);
    } else {
        console.log(data);
    }
});*/


