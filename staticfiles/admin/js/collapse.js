// 'use strict';
// {
//     const toggleVisibility = function(event) {
//         if (event.target.classList.contains('collapsed')) {
//             event.target.classList.remove('collapsed');
//         } else {
//             event.target.classList.add('collapsed');
//         }
//     };
//
//     const addToggleButtons = function(collapseFieldsets) {
//         collapseFieldsets.forEach(function(fieldset) {
//             const h2 = fieldset.querySelector('h2');
//             const toggleButton = document.createElement('button');
//             toggleButton.setAttribute('class', 'collapse-toggle');
//             toggleButton.setAttribute('type', 'button');
//             toggleButton.textContent = fieldset.classList.contains('collapsed') ? 'Show' : 'Hide';
//             h2.appendChild(document.createTextNode(' '));
//             h2.appendChild(toggleButton);
//
//             toggleButton.addEventListener('click', function(event) {
//                 event.preventDefault();
//                 if (fieldset.classList.contains('collapsed')) {
//                     fieldset.classList.remove('collapsed');
//                     toggleButton.textContent = 'less';
//                 } else {
//                     fieldset.classList.add('collapsed');
//                     toggleButton.textContent = 'more';
//                 }
//             }, { passive: true });
//
//             if (fieldset.classList.contains('collapsed')) {
//                 toggleButton.textContent = 'more';
//             } else {
//                 toggleButton.textContent = 'less';
//             }
//         });
//     };
//
//     window.addEventListener('load', function() {
//         const collapseFieldsets = document.querySelectorAll('fieldset.collapse');
//         collapseFieldsets.forEach(function(fieldset) {
//             fieldset.classList.add('collapsed'); // Add this line to ensure fieldsets are collapsed by default
//         });
//         addToggleButtons(collapseFieldsets);
//     }, { passive: true });
// }