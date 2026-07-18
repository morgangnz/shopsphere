import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Login() {

    const navigate = useNavigate();

    const { login } = useAuth();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    async function handleLogin() {

        try {

            await login(username, password);

            navigate("/products");

        }

        catch {

            alert("Usuario o contraseña incorrectos");

        }

    }

    return (

        <div style={{ padding: 40 }}>

            <h1>ShopSphere</h1>

            <h3>Iniciar sesión</h3>

            <input
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
                Entrar
            </button>

        </div>

    );

}

export default Login;