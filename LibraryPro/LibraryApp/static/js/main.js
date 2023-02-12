// Navbar
let menuList=document.getElementById("menuList")
menuList.style.maxHeight='0px'

function togglemenu(){
    if(menuList.style.maxHeight=='0px'){
        menuList.style.maxHeight='130px'
    }
    else{
        menuList.style.maxHeight='0px'
    }
}

// Adding New Student with user Validations
var password = document.getElementById('new-pass')
  , confirm_password = document.getElementById('confirm-new-pass');

// document.getElementById('signupLogo').src = "https://s3-us-west-2.amazonaws.com/shipsy-public-assets/shipsy/SHIPSY_LOGO_BIRD_BLUE.png";
enableSubmitButton();

function validatePassword() {
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
    return false;
  } else {
    confirm_password.setCustomValidity('');
    return true;
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

function enableSubmitButton() {
  document.getElementById('submitButton').disabled = false;
  document.getElementById('loader').style.display = 'none' ;
}

function disableSubmitButton() {
  document.getElementById('submitButton').disabled = true;
  document.getElementById('loader').style.display = 'unset';
}

function validateSignupForm(event) {
  event.preventDefault();
  var form = document.getElementById('signupForm');
  
  for(var i=0; i < form.elements.length; i++){
      if(form.elements[i].value === '' && form.elements[i].hasAttribute('required')){
        console.log('There are some required fields!');
        return false;
      }
    }
  
  if (!validatePassword()) {
    return false;
  }
  
}
