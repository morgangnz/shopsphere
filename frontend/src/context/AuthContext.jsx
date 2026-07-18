import { createContext, useContext, useState } from "react";
import * as authService from "../services/authService";

const AuthContext = createContext();

export function AuthProvider({ children }) {

    const [authenticated, setAuthenticated] = useState(
        authService.isAuthenticated()
    );

    async function login(username, password) {

        await authService.login(username, password);

        setAuthenticated(true);

    }

    function logout() {

        authService.logout();

        setAuthenticated(false);

    }

    return (

        <AuthContext.Provider
            value={{
                authenticated,
                login,
                logout
            }}
        >

            {children}

        </AuthContext.Provider>

    );

}

export function useAuth() {

    return useContext(AuthContext);

}