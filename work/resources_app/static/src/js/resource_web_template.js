const resources = document.querySelectorAll('.resources');

const themeButtons = document.querySelectorAll('.theme-btn');
const keywordButtons = document.querySelectorAll('.keyword-btn');
const universityButtons = document.querySelectorAll('.university-btn');

let selectedTheme = null;
let selectedKeywords = [];
let selectedUniversity = null;

resources.forEach((resource) => {
  const cardTitle = resource.querySelector('.card-title');
  const cardBody = resource.querySelector('.card-body');
  cardBody.classList.toggle('d-none');

  cardTitle.addEventListener('click', () => {
    cardBody.classList.toggle('d-none');
  });
});

function renderResources() {
  const resources = document.querySelectorAll('.resources');
  resources.forEach(resource => {
    const keywords = resource.dataset.keywords.split(",");
    const themes = resource.dataset.themes.split(",");
    const universities = resource.dataset.universities;
    console.log(universities);
    console.log(selectedUniversity);

    if ((selectedTheme === null || themes.includes(selectedTheme)) && (selectedUniversity === null || universities == selectedUniversity)){
      if(selectedKeywords.length == 0) {
        resource.classList.remove('d-none');
      } else {
        let found = false; 
        for(i = 0; i < selectedKeywords.length; i++) {
          if(keywords.includes(selectedKeywords[i])) {
            resource.classList.remove('d-none');
            found = true; 
          }
        }
        if(!found){
          resource.classList.add('d-none');
        }
      }
    } else {
      resource.classList.add('d-none');
    }
  });
}

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
    renderResources();
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
    renderResources();
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
    renderResources();
  });
});

//clear filter options initially
renderResources();