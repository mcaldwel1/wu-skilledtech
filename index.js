const arr = [
    "Name (First and Last)", 
    "Gender", 
    "Age", 
    "What is your race?", 
    "What is the highest degree or level of school that you have completed?", 
    "Are you currently employed?", 
    "Have you ever served on active duty in the U.S. Armed Forces, Reserves, or National Guard?"
];

const objarray = [
    "Nina Blackshear", 
    "Female", 
    "63", 
    "Black or African American", 
    "Some college, no degree", 
    "No", 
    "No"
];

const mappedData = arr.map((question, index) => {
    return { [question]: objarray[index] };
});

console.log(mappedData);