document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form from submitting the traditional way
  
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  
  // Basic placeholder for login functionality
  if (username && password) {
    alert(`Welcome, ${username}!`); // This can be replaced with real authentication
  } else {
    alert('Please enter both a username and password.');
  }
});
