from flask import Flask, request, jsonify, render_template_string
import os
import subprocess
import tempfile

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Python Code Runner</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f4; }
        textarea { width: 100%; height: 200px; font-family: monospace; }
        button { padding: 10px 20px; font-size: 16px; }
        pre { background: #333; color: #eee; padding: 10px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h2>Python Code Runner</h2>
    <form id="codeForm">
        <textarea id="codeInput" placeholder="Write your Python code here..."></textarea><br>
        <button type="submit">Run</button>
    </form>
    <h3>Output:</h3>
    <pre id="outputBox"></pre>

    <script>
        const form = document.getElementById('codeForm');
        const outputBox = document.getElementById('outputBox');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const code = document.getElementById('codeInput').value;

            const response = await fetch('/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code })
            });

            const data = await response.json();
            outputBox.textContent = data.output || data.error;
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/run', methods=['POST'])
def run_code():
    payload = request.get_json()
    if not payload or 'code' not in payload:
        return jsonify({'error': 'No code submitted'}), 400

    code = payload['code']

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py', mode='w') as tmp:
            tmp.write(code)
            temp_file_path = tmp.name

        result = subprocess.run(
            ['python', temp_file_path],
            capture_output=True,
            text=True,
            timeout=5 
        )

        os.remove(temp_file_path)

        if result.returncode == 0:
            return jsonify({'output': result.stdout})
        else:
            return jsonify({'error': result.stderr})

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Code execution timed out'}), 408
    except Exception as e:
        return jsonify({'error': f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=1010)
