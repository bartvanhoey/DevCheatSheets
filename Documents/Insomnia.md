## Insomnia by Kong

## How to chain requests using Insomnia

For example, get an AccessToken from Login Request for use in other request

### Create an Environment Variable

Press **CTRL+E** in the Insomnia workspace to open the **Manage Environments** window.

Add a variable like **access_token** to the environment. Put a response function (teal f) as value of this variable by pressing **CTRL+SPACE**.

Select one to your liking from the dropdown, in your case "Response => Body Attribute" should work well.

![Environment Variable](/Images/Insomnia_Environment_Variable.png "Environment Variable").

Click on the environment variable value and make the necessary edits.

![Edit Tag](/Images/Insomnia_Edit_Tag.png "Edit Tag").

### Make use of the Environment Variable

You can now access this variable anywhere in your workspace for other requests by pressing **CTRL+SPACE** in any form field and selecting the variable (purple x).

![Use of AccessToken](/Images/Insomnia_AccessToken.png "Use of AccessToken").
