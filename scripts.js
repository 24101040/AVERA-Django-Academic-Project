document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const menuButton = document.getElementById('menuButton');
    const navMenu = document.getElementById('navMenu');

    if (menuButton && navMenu) {
        menuButton.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }

    // 2. Animated Stats Counter (Portfolio Style Dynamic Numbers)
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        const target = +stat.getAttribute('data-target');
        let count = 0;
        const speed = target / 50;

        const updateCount = () => {
            count += speed;
            if (count < target) {
                stat.innerText = Math.ceil(count);
                setTimeout(updateCount, 30);
            } else {
                stat.innerText = target;
            }
        };
        updateCount();
    });

    // 3. Dynamic Filter Tabs (For Adoption, Wishlist or Features)
    const filterButtons = document.querySelectorAll('.filter-btn');
    const filterItems = document.querySelectorAll('.filter-item');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const category = btn.getAttribute('data-category');

            filterItems.forEach(item => {
                if (category === 'all' || item.getAttribute('data-category') === category) {
                    item.style.display = 'block';
                    item.style.animation = 'fadeIn 0.5s ease';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
});

// Dynamic Modal System for quick details view
function openModal(title, description) {
    const modal = document.getElementById('dynamicModal');
    if (modal) {
        document.getElementById('modalTitle').innerText = title;
        document.getElementById('modalBody').innerText = description;
        modal.style.display = 'flex';
    }
}

function closeModal() {
    const modal = document.getElementById('dynamicModal');
    if (modal) {
        modal.style.display = 'none';
    }
}