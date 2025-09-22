// Get the modal
const modal = document.getElementById("authModal");
const openModalBtn = document.getElementById("openModalBtn");
const closeBtn = document.getElementsByClassName("close")[0];

// Open the modal
openModalBtn.onclick = function() {
  modal.style.display = "block";
}

// Close the modal
closeBtn.onclick = function() {
  modal.style.display = "none";
}

// Close modal when clicking outside
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Tab functionality
function openTab(evt, tabName) {
  // Hide all tabcontent
  const tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove active class from all tablinks
  const tablinks = document.getElementsByClassName("tablinks");
  for (let i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }

  // Show the specific tab content and add active class to the button
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.classList.add("active");
}

// Form submission handlers
const loginForm = document.querySelector('#LoginForm form');
const signupForm = document.querySelector('#SignupForm form');

loginForm.addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Login functionality would be implemented here!');
  modal.style.display = "none";
});

signupForm.addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Sign up functionality would be implemented here!');
  modal.style.display = "none";
});