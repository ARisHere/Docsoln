const donationDate = document.querySelector('.donation__date');
const date = new Date();

const day = date.getDay();
const month = date.getMonth();
const year = date.getFullYear();

// console.log(`${day}/${month}/${year}`);
donationDate.innerHTML = `last donation date: ${day}/${month}/${year}`;
