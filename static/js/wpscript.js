//activate, publish, draft quotes
var csrfToken = document.getElementById('hCsrf').value;
var rawImgPrefix = document.getElementById('hRawImgPrefix').value;
var ver = document.getElementById('hVer').value;

function activate(id, isActive) {
let formData = new FormData();
    formData.append('id', id);
    formData.append('isActive', isActive);
    formData.append('csrfmiddlewaretoken', csrfToken);
    fetch("/wp-admin/activate",{
    body: formData,
    method: "post"
});
delDiv('qCardDiv' + id);
}
//schedule quotes
function schedule(id, isSchd) {
let formData = new FormData();
    formData.append('id', id);
    formData.append('isSchd', isSchd);
    formData.append('csrfmiddlewaretoken', csrfToken);
    fetch("/wp-admin/activate",{
    body: formData,
    method: "post"
});
delDiv('qCardDiv' + id);
}


function makeQuote(id) {
let formData = new FormData();
    formData.append('id', id);
    formData.append('csrfmiddlewaretoken', csrfToken);
    fetch("/wp-admin/make-quote",{
    body: formData,
    method: "post"
});
delDiv('qCardDiv' + id);

}

function prepareQuotes(id) {
let formData = new FormData();
    formData.append('id', id);
    formData.append('csrfmiddlewaretoken', csrfToken);
    fetch("/wp-admin/update",{
    body: formData,
    method: "post"
});
//console.log(id)
window.location.reload()

}

function delDiv(id) {
var myDiv = document.getElementById(id);
myDiv.remove();
}

function changeImg(id, imgId) {
var myImg = document.getElementById("raw-img-" + id);
var newImgId = document.getElementById(imgId).value;
myImg.src = rawImgPrefix + newImgId + ".jpg"
}
   
function callByUrl(type) {
  if(type === 'author'){
    fetch('/authors-list?isActive=0&v=' + ver ,{method: 'GET'}).then(res => res.json()).then(res => {
      localStorage.setItem('author', JSON.stringify(res));
    }).catch(err => console.log(err));
  };
   if(type === 'category'){
    fetch('/category-list?isActive=0&v=' + ver, {method: 'GET'}).then(res => res.json()).then(res => {
      localStorage.setItem('category', JSON.stringify(res));
    }).catch(err => console.log(err));
  }
   if(type === 'image'){
    fetch('/image-list?v=' + ver, {method: 'GET'}).then(res => res.json()).then(res => {
      localStorage.setItem('image', JSON.stringify(res));
    }).catch(err => console.log(err));
  }
   if(type === 'font'){
    fetch('/font-list?v=' + ver, {method: 'GET'}).then(res => res.json()).then(res => {
      localStorage.setItem('font', JSON.stringify(res));
    }).catch(err => console.log(err));
  }
}
function loadData() {
  callByUrl('author');
  callByUrl('category');
  callByUrl('image');
  callByUrl('font');
  window.location.reload();
}

function myOnLoad() {
  getAuthor();
  getCategory();
}

function getAuthor(){
  var authorList = localStorage.getItem('author');
  if (authorList == null || authorList == undefined) {
    callByUrl('author');
    authorList = localStorage.getItem('author');
  } else {
    var myDiv = document.getElementById('loadData');
    myDiv.remove();
  }
  authorList = JSON.parse(authorList);
    var list = document.getElementById('author');
    list.add(new Option('--Select--', ''));
    for (key in authorList) {
      var author = authorList[key].author;
      list.add(new Option(author, author));
    }
}
function getCategory(){
  var categoryList = localStorage.getItem('category');
  if (categoryList == null || categoryList == undefined) {
    callByUrl('category');
    categoryList = localStorage.getItem('category');
  }
  categoryList = JSON.parse(categoryList);
    var list = document.getElementById('category');
    list.add(new Option('--Select--', ''));
    for (key in categoryList) {
      var category = categoryList[key].category;
      list.add(new Option(category, category));
    }
}
function getImage(id){
  var imageList = localStorage.getItem('image');
  if (imageList == null || imageList == undefined) {
    callByUrl('image');
    imageList = localStorage.getItem('image');
  }
  imageList = JSON.parse(imageList);
    var list = document.getElementById('imageId-' + id);
    var oldImageId = document.getElementById('hImageId-' + id).value;
    for (key in imageList) {
      var imageId = imageList[key].id;
      var tags = imageList[key].tags;
      tags = tags.substring(0, 15);
      document.getElementById('imageTags-' + id).innerHTML = tags;
      if(imageId == oldImageId) {
        list.add(new Option(imageId + '-' + tags, imageId, false, true));
      } else {
        list.add(new Option(imageId + '-' + tags, imageId));
      }
    }
}

function getFont(id){
  var localeObj = {1:'English', 2:'हिन्दी', 4:'Bengali', 3:'اردو'};
  var fontList = localStorage.getItem('font');
  if (fontList == null || fontList == undefined) {
    callByUrl('font');
    fontList = localStorage.getItem('font');
  }
  fontList = JSON.parse(fontList);
    var list = document.getElementById('fontName-' + id);
    var oldFontName = document.getElementById('hFontName-' + id).value;
    var oldLocale = document.getElementById('hLocale-' + id).value;
    var newLocale = '';
    for (fontName in fontList) {
      locales = fontList[fontName];
      if (locales.length > 1) {
        for (i in locales) {
          newLocale = locales[i];
          localeName = localeObj[newLocale];
          //console.log('newLocale: ' + newLocale + ' | ' + localeName)
          if(fontName == oldFontName && oldLocale == newLocale) {
            list.add(new Option(fontName + '-' + localeName, fontName, false, true));
          } else {
            list.add(new Option(fontName + '-' + localeName, fontName));
          }
        }
      } else {
        newLocale = locales;
        localeName = localeObj[newLocale];
        if(fontName == oldFontName && oldLocale == newLocale) {
          list.add(new Option(fontName + '-' + localeName, fontName, false, true));
        } else {
          list.add(new Option(fontName + '-' + localeName, fontName));
        }
      }

    }
}

window.addEventListener('load', myOnLoad);