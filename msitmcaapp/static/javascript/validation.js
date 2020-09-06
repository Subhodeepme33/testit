function validation(){
	var fname = document.getElementById("inpt1").value;
	if(fname === '' || fname === null){
		alert("Firstname is missing");
		return false;
	}

// 	var lname = document.getElementById("inpt2").value;
// 	if(lname === '' || lname === null){
// 		alert("Lastname is missing");
// 		return false;
// 	}

	// var email=document.myform.email.value;  
	// var atposition=email.indexOf("@");  
	// var dotposition=email.lastIndexOf(".");  
	// if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){  
 //  		alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
 //  		return false;  
 //  	}

// 	var passwd = document.getElementById("inpt3").value;
// 	if(passwd === '' || passwd === null){
// 		alert("Lastname is missing");
// 		return false;
// 	}
// 	if(passwd.length <8 && passwd.length >15) {
// 		alert("Invalid length");
// 		return false;
// 	}

// // Phone Number Validation
// 	var phone = document.getElementById("inpt3").value;
// 	if(phone === '' || phone === null){
// 		alert("Phone number is missing");
// 		return false;
// 	}
// 	if(phone.length !== 10) {
// 		alert("Invalid length");
// 		return false;
// 	}
// 	if(isNaN(phone)) {
// 		alert("Invalid entry"):
// 		return false;
// 	}
}