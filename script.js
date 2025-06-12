// Efeitos interativos e animações
document.addEventListener('DOMContentLoaded', function() {
    // Animação suave para os corações
    createRandomHearts();
    
    // Efeito parallax nos elementos
    window.addEventListener('scroll', parallaxEffect);
    
    // Animação de digitação para a carta
    typeWriterEffect();
    
    // Efeito hover nas fotos
    setupPhotoEffects();
});

// Criar corações aleatórios
function createRandomHearts() {
    const heartsContainer = document.querySelector('.floating-hearts');
    const heartEmojis = ['❤️', '💕', '💖', '💗', '💘', '💝'];
    
    setInterval(() => {
        if (document.querySelectorAll('.random-heart').length < 10) {
            const heart = document.createElement('div');
            heart.className = 'heart random-heart';
            heart.textContent = heartEmojis[Math.floor(Math.random() * heartEmojis.length)];
            heart.style.left = Math.random() * 100 + '%';
            heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
            heart.style.fontSize = (Math.random() * 10 + 15) + 'px';
            
            heartsContainer.appendChild(heart);
            
            // Remove o coração após a animação
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 8000);
        }
    }, 2000);
}

// Efeito parallax suave
function parallaxEffect() {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.love-letter, .photo-gallery, .final-message');
    
    parallaxElements.forEach((element, index) => {
        const speed = 0.1 * (index + 1);
        element.style.transform = `translateY(${scrolled * speed}px)`;
    });
}

// Efeito de digitação (typewriter) - opcional
function typeWriterEffect() {
    // Este efeito pode ser aplicado a parágrafos específicos se desejado
    const elementsToType = document.querySelectorAll('.letter-content p');
    
    // Uncomment below to enable typewriter effect
    /*
    elementsToType.forEach((element, index) => {
        const text = element.textContent;
        element.textContent = '';
        element.style.borderRight = '2px solid #d63384';
        
        setTimeout(() => {
            typeText(element, text, 0);
        }, index * 2000);
    });
    */
}

function typeText(element, text, index) {
    if (index < text.length) {
        element.textContent += text.charAt(index);
        setTimeout(() => typeText(element, text, index + 1), 50);
    } else {
        element.style.borderRight = 'none';
    }
}

// Configurar efeitos das fotos
function setupPhotoEffects() {
    const photoFrames = document.querySelectorAll('.photo-frame');
    
    photoFrames.forEach(frame => {
        frame.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) rotate(' + (Math.random() * 6 - 3) + 'deg) scale(1.05)';
        });
        
        frame.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) rotate(0deg) scale(1)';
        });
        
        // Adiciona brilho quando a foto carrega
        const img = frame.querySelector('img');
        if (img) {
            img.addEventListener('load', function() {
                frame.classList.add('photo-loaded');
                frame.style.animation = 'photoAppear 0.8s ease-out';
            });
        }
    });
}

// Adicionar partículas de coração no clique
document.addEventListener('click', function(e) {
    createClickHearts(e.clientX, e.clientY);
});

function createClickHearts(x, y) {
    for (let i = 0; i < 6; i++) {
        const heart = document.createElement('div');
        heart.textContent = '💕';
        heart.style.position = 'fixed';
        heart.style.left = x + 'px';
        heart.style.top = y + 'px';
        heart.style.pointerEvents = 'none';
        heart.style.fontSize = '20px';
        heart.style.zIndex = '1000';
        heart.style.animation = `clickHeart 1.5s ease-out forwards`;
        heart.style.transform = `rotate(${Math.random() * 360}deg)`;
        
        document.body.appendChild(heart);
        
        // Remove após animação
        setTimeout(() => {
            if (heart.parentNode) {
                heart.parentNode.removeChild(heart);
            }
        }, 1500);
    }
}

// Adiciona CSS para animação de clique
const style = document.createElement('style');
style.textContent = `
    @keyframes clickHeart {
        0% {
            opacity: 1;
            transform: scale(0.8) translateY(0px);
        }
        100% {
            opacity: 0;
            transform: scale(1.5) translateY(-50px);
        }
    }
    
    @keyframes photoAppear {
        from {
            opacity: 0;
            transform: scale(0.8);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    .photo-loaded {
        position: relative;
    }
    
    .photo-loaded::after {
        content: '✨';
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 20px;
        animation: sparkle 2s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
        50% { opacity: 0.7; transform: scale(1.2) rotate(180deg); }
    }
`;
document.head.appendChild(style);

// Música de fundo (opcional - descomente se quiser adicionar)
/*
function playBackgroundMusic() {
    const audio = new Audio('musica-romantica.mp3'); // Adicione um arquivo de música
    audio.loop = true;
    audio.volume = 0.3;
    
    // Reproduzir após interação do usuário (requisito dos navegadores)
    document.addEventListener('click', function() {
        audio.play().catch(e => console.log('Não foi possível reproduzir a música'));
    }, { once: true });
}
*/
