const API_URL = "http://localhost:8000/tasks/";

// Charger les tâches
async function loadTasks() {
    const response = await fetch(API_URL);
    const tasks = await response.json();
  
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";
  
    tasks.forEach(task => {
      const li = document.createElement("li");
      li.innerHTML = `
        <span><strong>${task.title}</strong>: ${task.description}</span>
        <button onclick="deleteTask('${task._id}')">Supprimer</button>
      `;
      taskList.appendChild(li);
    });
  }
  

// Ajouter une tâche
async function addTask(event) {
    event.preventDefault();
  
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
  
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description }) // Exclut explicitement l'_id
    });
  
    const newTask = await response.json();
    console.log("Nouvelle tâche ajoutée :", newTask); // Pour vérifier
    document.getElementById("task-form").reset();
    loadTasks();
  }  
  

// Supprimer une tâche
async function deleteTask(id) {
    console.log("Suppression de la tâche avec ID :", id); // Vérifiez l'ID ici
    await fetch(`${API_URL}${id}`, { method: "DELETE" });
    loadTasks();
  }  

// Événements
document.getElementById("task-form").addEventListener("submit", addTask);
window.onload = loadTasks;
