let resources = document.querySelectorAll('.resources');
const themeButtons = document.querySelectorAll('.theme-btn');
const keywordButtons = document.querySelectorAll('.keyword-btn');
const universityButtons = document.querySelectorAll('.university-btn');

let selectedTheme = null;
let selectedKeywords = [];
let selectedUniversity = null;

let page = 1; 

function requestInfrastructures() {
  let data = {
    'page': page,
  };
  if (selectedTheme) {
    data['theme'] = selectedTheme;
  }
  if (selectedKeywords.length > 0) {
    console.log(selectedKeywords);
    data['keywords'] = selectedKeywords.join(',');
  }
  if (selectedUniversity) {
    data['university'] = selectedUniversity;
  }

  $.ajax({
    type: "POST",
    url: "/resources/infrastructure/filtered",
    data: data,
    success: function(data) {

      $('#infrastructures-container').html(data);
      updateFunctions();
    },
    error: function(xhr, textStatus, errorThrown) {
        console.log(textStatus + ': ' + errorThrown);
    }
  });
}

function updateFunctions() {
  resources = document.querySelectorAll('.resources');

  resources.forEach((resource) => {
    const cardTitle = resource.querySelector('.card-title');
    const cardBody = resource.querySelector('.card-body');
    cardBody.classList.toggle('d-none');
  
    cardTitle.addEventListener('click', () => {
      cardBody.classList.toggle('d-none');
    });
  });
  
  $('.left-btn').click(function() {
    if (page > 1) {
      page = page - 1;
      requestInfrastructures();
    }
  });

  $('.right-btn').click(function() {
    if (page < document.querySelector('.products_pager').dataset.max) {
      page = page + 1;
      requestInfrastructures();
    }
  });
}

$(document).ready(function() {
  $('.filter-btn').click(function() {
    page = 1;
    requestInfrastructures();
  });
});

themeButtons.forEach(button => {
  button.addEventListener('click', () => {
    if (button.classList.contains('selected')) {
      button.classList.remove('selected');
      selectedTheme = null;
    } else {
      themeButtons.forEach(btn => btn.classList.remove('selected'));
      button.classList.add('selected');
      selectedTheme = button.dataset.theme;
    }
  });
});

keywordButtons.forEach(button => {
  button.addEventListener('click', () => {
    if (button.classList.contains('selected')) {
      button.classList.remove('selected');
      selectedKeywords = selectedKeywords.filter(keyword => keyword !== button.dataset.keyword);
    } else {
      button.classList.add('selected');
      selectedKeywords.push(button.dataset.keyword);
    }
  });
});

universityButtons.forEach(button => {
  button.addEventListener('click', () => {
    if (button.classList.contains('selected')) {
      button.classList.remove('selected');
      selectedUniversity = null;
    } else {
      universityButtons.forEach(btn => btn.classList.remove('selected'));
      button.classList.add('selected');
      selectedUniversity = button.dataset.university;
    }
  });
});

//request infrastructures initially
requestInfrastructures();
