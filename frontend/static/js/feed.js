// Get token from localStorage
const token = localStorage.getItem('token');

if (!token) {
    window.location.href = "login.html";
}

const feedContainer = document.getElementById('feedContainer');

async function loadFeed() {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/feed/feed/', {
            headers: {
                'Authorization': `Token ${token}`
            }
        });

        if (res.status === 200) {
            const data = await res.json();
            displayPosts(data.results || data);
        } else if (res.status === 403 || res.status === 401) {
            alert("Authentication required");
            window.location.href = "login.html";
        } else {
            console.error("Error fetching feed", res);
        }
    } catch (err) {
        console.error(err);
    }
}

function displayPosts(posts) {
    feedContainer.innerHTML = '';
    posts.forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';
        postDiv.innerHTML = `
            <h3>${post.user.username}</h3>
            <p>${post.caption}</p>
            ${post.image ? `<img src="${post.image}" />` : ''}
            <p>Likes: ${post.likes_count || 0}</p>
        `;
        feedContainer.appendChild(postDiv);
    });
}

loadFeed();

// Logout button
document.getElementById('logoutBtn').addEventListener('click', () => {
    localStorage.removeItem('token');
    window.location.href = "login.html";
});
