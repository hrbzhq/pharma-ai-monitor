async function fetchStatus(){
  try{
    const r = await fetch('/api/stats');
    const j = await r.json();
    document.getElementById('status').textContent = JSON.stringify(j, null, 2);
  }catch(e){
    document.getElementById('status').textContent = '无法获取状态: '+e.message
  }
}
document.getElementById('refresh').addEventListener('click', fetchStatus);
window.addEventListener('load', fetchStatus);
