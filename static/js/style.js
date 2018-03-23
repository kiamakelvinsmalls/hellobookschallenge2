function login(){
  document.getElementById('login').style.display="block";
}

function shut(){
  document.getElementById('login').style.display="none";
  document.getElementById('signup').style.display="none";
  document.getElementById('adminLogin').style.display="none";
  document.getElementById('adminSignup').style.display="none";

 }
function signup(){
  document.getElementById('signup').style.display="block";
}

function clientDetails(){
	document.getElementById('clientDetails').style.display='block';
}
function dismiss(){
	document.getElementById('clientDetails').style.display="none";
  document.getElementById('clientView').style.display="none";
}
function adminSignup(){
  document.getElementById('adminSignup').style.display="block";
}

function adminLogin(){
	document.getElementById('adminLogin').style.display='block';
}

function deleteSubmit() {
  var name=document.getElementById('name').value;
  var author=document.getElementById('author').value;
  var qty =document.getElementById('qty').value;

  return confirm('confirm to delete ' + qty + ' copy of ' + name +' by '+author +' from shelf');
}

function addSubmit(){
	var name=document.getElementById('name').value;
    var author=document.getElementById('author').value;
    var qty =document.getElementById('qty').value;

    return  confirm(qty + " copy of " +name + " by "+ author +" has be added to self ");

}
function clientView(){
  document.getElementById('clientView').style.display='block';
}

var firstname = document.getElementById('firstname');
var lastname = document.getElementById('lastname');
var email=document.getElementById('email');
var phoneno=document.getElementById('phoneno');
var pswd=document.getElementById('pswd');
var idNo=document.getElementById('idNo')
///store the details
function store() {
    localStorage.setItem('firstname', firstname.value);
    localStorage.setItem('lastname', lastname.value);
    localStorage.setItem('email', email.value);
    localStorage.setItem('phoneno', phoneno.value);
    localStorage.setItem('pswd', pswd.value);
    localStorage.setItem('idNo', idNo.value);

    alert("account created please login")


}
//validate for login
function check() {

    // stored data from the register-form
    var storedidNo = localStorage.getItem('idNo');
    var storedpswd = localStorage.getItem('pswd');

    // entered data from the login-form
    var useridNo = document.getElementById('useridNo');
    var userpswd = document.getElementById('userpswd');

    // check if user info is correct
    if(useridNo.value !== storedidNo || userpswd.value !== storedpswd) {
        alert('wrong credentials or account does not exist');
        return false
    }
    else {
        alert('welcome to B.I.G Resource Center');
        return true;
    }
}


