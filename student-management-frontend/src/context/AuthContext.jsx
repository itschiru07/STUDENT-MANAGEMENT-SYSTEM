/* eslint-disable react-refresh/only-export-components */
import { createContext, useState } from "react";
import api from "../api/axios";

export const AuthContext = createContext();

export function AuthProvider({ children }) {

    const [user, setUser] = useState(() => {
        const token = localStorage.getItem("access");
        return token ? { token } : null;
    });

    const [loading] = useState(false);

    const login = async (username, password) => {

        try {

            const response = await api.post(
                "/token/",
                {
                    username,
                    password,
                }
            );

            localStorage.setItem(
                "access",
                response.data.access
            );

            localStorage.setItem(
                "refresh",
                response.data.refresh
            );

            setUser({
                token: response.data.access,
            });

            return {
                success: true,
            };

        }

        catch {

            return {
                success: false,
            };

        }

    };

    const logout = () => {

        localStorage.removeItem("access");

        localStorage.removeItem("refresh");

        setUser(null);

    };

    return (

        <AuthContext.Provider
            value={{
                user,
                login,
                logout,
                loading,
            }}
        >

            {children}

        </AuthContext.Provider>

    );

}