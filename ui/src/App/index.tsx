import { useContext } from "react";
import { PortfolioBuilder } from "../PortfolioBuilder";
import * as classes from './app.module.css';
import { CreateUserForm } from "../CreateUserForm";
import { AppContext } from "../Context";

export function App() {
    const {
        users,
        hasPortfolio,
        portfolios,
        createUser,
        createPortfolio,
        fetchPortfolios,
        currentUser,
        setCurrentUser
    } = useContext(AppContext)

    return currentUser > 0 ? (
        <div className={classes.app_container}>
            <h1>Hello User {currentUser}</h1>
            <button onClick={() => setCurrentUser(0)}>Logout</button>
            {
                portfolios.length > 0 ? portfolios.map((p) => (
                    <PortfolioBuilder key={p.portfolio.id} portfolio={p} userId={currentUser} onCreatePortfolio={fetchPortfolios} hasPortfolio={hasPortfolio} />
                )) :
                    <div>
                        <button onClick={createPortfolio}>Create Portfolio</button>
                    </div>
            }
        </div>
    ) : (
        <div>
            <CreateUserForm onCreateUser={createUser} />
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
