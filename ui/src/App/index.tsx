import { useState, useEffect } from "react";
import { PortfolioBuilder } from "../PortfolioBuilder";
import * as classes from './app.module.css';
import { CreateUserForm } from "../CreateUserForm";

export function App() {
    const [portfolios, setPortfolios] = useState<any[]>([]);
    const [hasPortfolio, setHasPortfolio] = useState<boolean>(false);
    const [users, setUsers] = useState<any[]>([]);
    const [currentUser, setCurrentUser] = useState(0);

    useEffect(() => {
        fetchPortfolios();
        fetchUsers();
    }, [])

    useEffect(() => {
        fetchPortfolios();
    }, [currentUser])
    
    const fetchPortfolios = async () => {
        const res = await fetch(`http://localhost:8000/portfolio/${currentUser}/`)
        const json = await res.json();
        setHasPortfolio(json.length > 0)
        setPortfolios(json);
    }
    
    const fetchUsers = async () => {
        const res = await fetch(`http://localhost:8000/user/`)
        const json = await res.json();

        setUsers(json);
    }

    const createPortfolio = () => {
        setPortfolios([...portfolios, { currencies: [], portfolio: {} }])
    }

    const createUser = async (username: string, password: string) => {
        await fetch(`http://localhost:8000/user/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })

        await fetchUsers();
    }

    return currentUser > 0 ? (
        <div className={classes.app_container}>
            <h1>Hello User {currentUser}</h1>
            <button onClick={() => setCurrentUser(0)}>Logout</button>
            {
                portfolios.length > 0 ? portfolios.map((p) => (
                    <PortfolioBuilder key={p.id} portfolio={p} userId={currentUser} onCreatePortfolio={fetchPortfolios} hasPortfolio={hasPortfolio}/>
                )) :
                <div>
                    <button onClick={createPortfolio}>Create Portfolio</button>
                </div>
            }
        </div>
    ) : (
        <div>
            <CreateUserForm onCreateUser={createUser}/>
            <div>
                {
                    users.map((u) => (
                        <button onClick={() => setCurrentUser(u.id)}>{u.id}</button>
                    ))
                }
            </div>
        </div>
    )
}