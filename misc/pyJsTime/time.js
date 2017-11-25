function Date2String (dateObj) {
	return dateObj.toJSON();
}

function String2Date (stringObj) {
	var date = new Date(stringObj);
	return date;
}

// TESTING CODE

// a = new Date();
// console.log(Date2String(a));

// var c = String2Date("2017-11-25T12:45:10.434Z");
// console.log(c);

// TESTING CODE