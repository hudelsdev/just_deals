function openCity(evt, cityName) {
  var i, tabcontent, tablinks;

  // Hide all tab content
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display   
= "none";
  }

  // Remove active class from all tab links
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace("   
active", "");
  }

  // Show the current tab content and add active class to the clicked   
tab
  document.getElementById(cityName).style.display = "block";
  if (evt) {
      evt.currentTarget.className += " active";
  }
}

// Automatically open the "DEALS" tab on page load
window.onload = function() {
  var defaultTab = document.querySelector(".tablinks");
  if (defaultTab) {
      // Open the "DEALS" tab directly without needing to simulate a click event
      openCity(null, 'London');
      // Ensure the default tab gets the active class
      defaultTab.className += " active";
  }
};