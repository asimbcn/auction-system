const form = document.getElementById('form');
const username = document.getElementById('username');
const password = document.getElementById('password');
let success = '';

form.addEventListener('submit', e => {
	e.preventDefault();
	success = ''
	checkInputs();
	if(success === 'AD'){
		e.currentTarget.submit();
	}
   
});

function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const passwordValue = password.value.trim();
	
	if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	} else {
		setSuccessFor(username);
		success += 'A'
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	} else {
		setSuccessFor(password);
		success += 'D'
	}
	

}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
	
}
	
