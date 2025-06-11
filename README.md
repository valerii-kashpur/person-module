# Website Persons Module for Odoo 16 📋

**Manage and display person records on your Odoo website with ease!**

The *Website Persons* module extends the Odoo 16 Website module to provide a simple yet powerful way to manage and
display person records in both the backend and frontend. It allows administrators to create and manage person records in
the Odoo backend and enables website visitors to view a list of persons or add new ones via a user-friendly web
interface. 🎉

---

## ✨ Features

### Backend Features

- **Persons Model**:
    - A custom model `website.persons` to store person records with the following fields:
        - `first_name` (required): The person's first name.
        - `last_name` (required): The person's last name.
        - `full_name` (computed): Concatenation of first and last names.
        - `birthday`: Date field for the person's birthday.
        - `age` (computed): Automatically calculated based on the birthday.
        - `sex`: Selection field (Male, Female, Non-binary).
        - `company_id` (required): Many2one relation to `res.company`, defaulting to the current user's company.
    - Computed fields (`full_name` and `age`) are automatically updated based on input data.
- **Backend Views**:
    - **List View**: Displays all person records in a table format with all fields.
    - **Form View**: Allows creating and editing person records with a clean, organized layout.
- **Menu Integration**:
    - A dedicated menu item under *Website > Configuration > Persons* to access the list of persons in the backend.

### Frontend Features

- **Persons List Page** (`/persons`):
    - Displays the 5 most recent person records as Bootstrap-styled cards.
    - Each card shows:
        - Full name
        - Sex (if selected)
        - Age
        - Company name
    - Includes a button to navigate to the "Add New Person" page.
- **Add Person Form** (`/persons/add`):
    - A web form to create new person records, accessible to public users.
    - Fields include:
        - First Name (required)
        - Last Name (required)
        - Birthday
        - Sex (dropdown with Male, Female, Non-binary options)
        - Company (dropdown populated with available companies)
    - Submits data to create a new record and redirects to the persons list.

### Security

- Configurable access rights:
    - Internal users (`base.group_user`) have full access (read, write, create, delete).
    - Public users (`base.group_public`) have read-only access to person records.
- Uses `sudo()` in the controller to ensure public access to the frontend functionality.

---

## 🛠️ Installation

1. **Clone or Download the Module**:
    - Clone this repository or download the module folder (`website_persons`) to your Odoo addons directory:
      ```bash
      git clone <repository_url> /path/to/odoo/addons/website_persons
      ```
    - Alternatively, place the module folder in your custom addons path.

2. **Update the Odoo Addons Path**:
    - Ensure the module folder is in the Odoo addons path. Update your Odoo configuration file (`odoo.conf`) if needed:
      ```conf
      addons_path = /path/to/odoo/addons,/path/to/custom/addons
      ```

3. **Install Dependencies**:
    - The module depends on the `website` and `base` modules, which are included in Odoo 16 by default.

4. **Update the Modules List**:
    - Start your Odoo instance and update the modules list:
        - Go to *Apps* in the Odoo backend.
        - Click *Update Apps List* to make the module visible.

5. **Install the Module**:
    - In the *Apps* menu, search for *Website Persons*.
    - Click *Install* to activate the module.

---

## 📖 Usage

### Backend Usage

1. **Access the Persons Menu**:
    - Log in to the Odoo backend as an administrator or a user with appropriate permissions.
    - Navigate to *Website > Configuration > Persons* to view the list of persons.
2. **Manage Persons**:
    - Use the list view to see all person records.
    - Click on a record or select *Create* to open the form view for editing or adding a new person.
    - Fill in the required fields (`first_name`, `last_name`, `company_id`) and optional fields (`birthday`, `sex`).
    - The `full_name` and `age` fields are automatically computed.

### Frontend Usage

1. **View the Persons List**:
    - Visit `/persons` on your Odoo website (e.g., `http://your-odoo-site/persons`).
    - See the 5 most recent person records displayed as cards.
2. **Add a New Person**:
    - Click the *Add New Person* button on the `/persons` page to go to `/persons/add`.
    - Fill out the form with the required fields and submit.
    - After submission, you’ll be redirected to the `/persons` page to see the updated list.

---

## 🗂️ Module Structure

```plaintext
website_persons/
├── __init__.py
├── __manifest__.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── persons_views.xml
│   └── website_templates.xml
├── controllers/
│   └── __init__.py
│   └── main.py
└── models/
    └── __init__.py
    └── persons.py
```

- `__manifest__.py`: Module metadata and dependencies.
- `security/ir.model.access.csv`: Access rights for the `website.persons` model.
- `views/persons_views.xml`: Backend views (list and form) and menu configuration.
- `views/website_templates.xml`: Frontend QWeb templates for the persons list and add form.
- `controllers/main.py`: HTTP controller for handling `/persons` and `/persons/add` routes.
- `models/persons.py`: Definition of the `website.persons` model with fields and computed logic.

---

## 🔧 Technical Details

- **Odoo Version**: 16
- **Dependencies**: `website`, `base`
- **Model**: `website.persons`
- **Frontend Routes**:
    - `/persons`: Displays the 5 most recent persons.
    - `/persons/add`: Handles the creation of new person records.
- **QWeb Templates**:
    - `persons_list_template`: Renders the persons list page.
    - `persons_add_template`: Renders the add person form.
- **Access Control**:
    - Public users can view the persons list.
    - Internal users can manage records in the backend.

---

## 🚀 Development Notes

### Potential Improvements

- **Form Validation**: Add client-side and server-side validation for required fields in the add person form.
- **Error Handling**: Display user-friendly error messages if form submission fails.
- **Styling**: Enhance the frontend templates with additional CSS for better responsiveness and visual appeal.
- **Filtering/Sorting**: Add options to filter or sort the persons list on the frontend.

### Known Limitations

- The module assumes the presence of companies in the `res.company` model for the `company_id` field.
- No pagination is implemented for the frontend list (limited to 5 records).

---

*Happy managing your persons with Odoo! 🚀*
