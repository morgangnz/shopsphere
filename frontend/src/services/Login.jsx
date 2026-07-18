import { useState } from "react";
import { login } from "../services/authService";

function Login() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    async function handleLogin() {

        try {

            const data = await login(username, password);

            console.log(data);

        } catch (error) {

            console.error(error);

            alert("Usuario o contraseña incorrectos");

        }

    }

    return (
        <div>
            <h2>Login</h2>

            <input
                type="text"
                placeholder="Usuario"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />

            <br /><br />

            <input
                type="password"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <br /><br />

            <button onClick={handleLogin}>
                Iniciar sesión
            </button>

        </div>
    );

}

export default Login;