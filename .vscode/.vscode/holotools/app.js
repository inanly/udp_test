document.addEventListener('DOMContentLoaded', () => {
    const url = 'AIzaSyCoXo1cxCZrE65us6ZtDLO5YQv4r3KwtU4'; // 将此 URL 替换为您的 Google Cloud 公共 API 端点
    const resultsElement = document.getElementById('results');

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // 在这里处理返回的数据
            // 例如，将数据显示在页面上：
            resultsElement.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            resultsElement.innerHTML = 'Error: Unable to fetch data';
        });
});
