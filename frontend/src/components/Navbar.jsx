import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Navbar() {

    const { logout } = useAuth();

    return (

        <nav
            style={{
                display: "flex",
                gap: "20px",
                padding: "20px",
                background: "#222",
                color: "white"
            }}
        >

            <Link to="/products">Productos</Link>

            <Link to="/categories">Categorías</Link>

            <Link to="/dashboard">Dashboard</Link>

            <button onClick={logout}>
                Cerrar sesión
            </button>

        </nav>

    );

}

export default Navbar;