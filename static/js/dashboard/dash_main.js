// document.addEventListener('DOMContentLoaded', () => {
//     const token = localStorage.getItem('token');

//     // if (!token) {
//     //     // Redirect to login if no token is found
//     //     window.location.href = '/login.html';
//     //     return;
//     // }

//     // Fetch user-specific dashboard data
//     fetch('/api/dashboard', {
//         method: 'GET',
//         headers: {
//             'Authorization': `Bearer ${token}`,
//             'Content-Type': 'application/json'
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Use the data to populate the dashboard
//         document.getElementById('username').innerText = data.username;
//         document.getElementById('account-balance').innerText = data.balance;
//         // Populate other user-specific information
//     })
//     .catch(error => {
//         console.log('Error fetching dashboard data:', error);
//         alert('Failed to load dashboard data. Please try again later.');
//     });
// });