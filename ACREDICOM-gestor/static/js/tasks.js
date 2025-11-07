
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return decodeURIComponent(parts.pop().split(';').shift());
}

document.addEventListener('change', function (e) {
  if (e.target.classList.contains('js-status')) {
    const tr = e.target.closest('tr[data-task-id]');
    const taskId = tr.getAttribute('data-task-id');
    const estado = e.target.value;
    fetch(`/tasks/${taskId}/change-status/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Accept': 'application/json',
      },
      body: new URLSearchParams({estado})
    }).then(r => r.json())
      .then(data => {
        if (!data.ok) {
          alert(data.error || 'Error al actualizar estado');
        }
      })
      .catch(() => alert('Error de red'));
  }
});
