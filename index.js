const substr = "Pre-Course";

var data = [{"id":"66984a68f9dbb9614d08de16",
    "type":"pbEbook",
    "icon":"ebook",
    "title":"Welcome toUnleashing the Power of AI: Empowering Educators Everywhere!",
    "subtitle":"ebook"},
    {"id":"66984bff0add8f175f0875af",
        "type":"newSurvey",
        "icon":"survey",
        "title":"Getting to Know You",
        "subtitle":"Introduce yourself"},
        {"id":"6697bcff68908739df06b18a",
            "type":"pdf",
            "icon":"pdf",
            "title":"Meet the Instructors","subtitle":"pdf"},
            {"id":"6697bcff68908739df06b18c",
                "type":"assessmentV2",
                "icon":"quiz",
                "title":"Pre-Course Assessment",
                "subtitle":"Self-Assessment"}];

var result = data.filter(function getPreCourse(data) {return data.title.includes(substr)});

console.log(result);
console.log(result[0].id);

return result[0].id;

/*function getPreCourse(data, reg) {
    return data.filter(
        function(reg, data) {return reg.includes(data.title)}
    );
}

const result = getPreCourse(data, substr);
console.log(result);*/