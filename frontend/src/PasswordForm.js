import React from 'react';
import { ValidatorForm, TextValidator} from 'react-material-ui-form-validator';
import TextField from "@material-ui/core/TextField";

export default class PasswordForm extends React.Component {

    state = {
        password: '',
    };

    componentDidMount() {
        ValidatorForm.addValidationRule('contains-vowel', (value) => {
            const vowels = ['a', 'e', 'i', 'o', 'u'];
            for (let i = 0; i < vowels.length; i++) {
                if (value.includes(vowels[i])) {
                    return true;
                }
            }
            return false;
        });

        ValidatorForm.addValidationRule('min-length-6', (value) => {
            return value.length >= 6;
        });
    };

    componentWillUnmount() {
        ValidatorForm.removeValidationRule('contains-vowel');
    };

    handleChange = (event) => {
        let { password } = this.state;
        password = event.target.value;
        this.setState({password});
    };

    handleSubmit = () => {
    };

    render() {
        const {password} = this.state;

        return (
            <ValidatorForm
                onSubmit={this.handleSubmit}
            >
                <TextValidator
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="password"
                    label="Password"
                    name="password"
                    type="password"
                    autoFocus
                    onChange={this.handleChange}

                    validators={['min-length-6', 'contains-vowel']}
                    errorMessages={['password must be at least 6 characters long', 'password must contain a vowel']}
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
            </ValidatorForm>
        );
    }
}