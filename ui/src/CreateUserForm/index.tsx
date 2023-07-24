import { useState } from "react"

type Props = {
    onCreateUser: (username: string, password: string) => void;
}

export function CreateUserForm({ onCreateUser }: Props) {
    const [username, setUsername] = useState<string>("")
    const [password, setPassword] = useState<string>("")

    const handleClick = () => {
        if(username.length === 0 || password.length === 0) {
            alert("Username and password are required")
            return;
        }
        onCreateUser(username, password)
    }

    return (
        <div>
            <input placeholder="username" value={username} onChange={e => setUsername(e.target.value)}/>
            <input placeholder="password" type="password" value={password} onChange={e => setPassword(e.target.value)}/>
            <button onClick={handleClick}>Create User</button>
        </div>
    )
}