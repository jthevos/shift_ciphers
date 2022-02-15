let document = raw_html.html

let table_rows = document.getElementsByClassName("table__row")

let arr = [].slice.call(table_rows);

let names = []

for (i=0;i<arr.length;i++) {
    let x = arr[i].replace(/\W/g, '')
    names.push(x.slice(0,5))
    names.push(x.slice(-5))
}

rows = document.getElementsByClassName("table__row")
words = []
output = []
count = 0;
for (i = 0; i < rows.length; i++) {
    words.push(rows[i].innerText.replace(/\W/g, '').slice(0,5))
}

for (i = 0; i < words.length; i++) {
  count++;
  output.push(count);
  output.push(": ");
  output.push("\"");
  output.push(names[i]);
  output.push("\"");
  output.push(",");
  output.push("\n");
}

// copy and paste this into your browser console
// to avoid hand-copying the scales from
// http://www.microtonal-synthesis.com/scales.html

// this script will output what is to be copied into a python dictionary

// BEGIN COPY
names = [];
count = 0;
buffer = [];
table_data = document.getElementsByTagName("tr");

arr = [].slice.call(table_data);

for (i=0;i<arr.length;i++) {
    let x = arr[i].replace(/\W/g, '')
    names.push(x.slice(0,5))
    names.push(x.slice(-5))
}


for (i = 0; i < names.length; i++) {
  count++;
  buffer.push(count);
  buffer.push(": ");
  buffer.push("\"");
  buffer.push(names[i]);
  buffer.push("\"");
  buffer.push(",");
  buffer.push("\n");
}

console.log(buffer.join(""));
// END COPY

names = [];
count = 0;
buffer = [];
table_data = document.getElementsByTagName("tr");

arr = [].slice.call(table_data);

for (i=0;i<arr.length;i++) {
    x = arr[i].innerText.replace(/\W/g, '')
    names.push(x.slice(0,5))
    names.push(x.slice(-5))
}

for (i = 0; i < names.length; i++) {
  buffer.push(names[i]);
  buffer.push(",");
}
console.log(buffer.join(""));

for (i = 0; i < names.length; i++) {
  count++;
  buffer.push(count);
  buffer.push(": ");
  buffer.push("\"");
  buffer.push(names[i]);
  buffer.push("\"");
  buffer.push(",");
  buffer.push("\n");
}

console.log(buffer.join(""));
