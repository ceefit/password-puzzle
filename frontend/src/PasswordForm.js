import React from 'react';
import TextField from "@material-ui/core/TextField";

export default class PasswordForm extends React.Component {
    state = {
        password: '',
        isValid: false,
        errorMessage: ''
    };

    componentDidMount() {
    };

    componentWillUnmount() {
    };

    handleChange = (event) => {
        const { REACT_APP_API_HOST } = process.env;

        let password = event.target.value;
        this.setState({password});

        let data = {'user_id': 'some dood',
                    'password': password};

        fetch(REACT_APP_API_HOST + '/check-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
          }).then(res => res.json())
            .then(json => this.setState( json ));
    };

    render() {
        const {password, isValid, errorMessage} = this.state;

        return (
            <React.Fragment>
                <TextField
                    error={!isValid}
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="password"
                    label="Password"
                    name="password"
                    type="password"
                    helperText={errorMessage}
                    autoFocus
                    onChange={this.handleChange}
                    value={password}
                />
                <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="repeat_password"
                    label="Repeat Password"
                    name="repeat_password"
                    type="password"
                />
            </React.Fragment>

        );
    }
}