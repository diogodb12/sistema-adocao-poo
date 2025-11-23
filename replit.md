# Overview

This is a Pet Adoption Management System built in Python. The application manages pet registrations and adoptions through a console-based menu interface. It allows users to register pets found on the streets, track their information, manage adopters, and process adoptions. The system uses CSV files for data persistence, storing pet records and adopter information separately.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Application Structure

The system follows an object-oriented architecture with a simple class-based design:

- **Main Entry Point (`main.py`)**: Provides the application loop that displays menu options and routes user selections to appropriate handlers
- **Class-Based Modules**: Core business logic is separated into distinct classes (Menu, Pet, Pessoa) within the `classes/` package
- **Text-Based Configuration**: Menu options and form questions are stored in external text files (`texts/`) for easy modification without code changes

## Data Model

The application uses two primary domain objects:

1. **Pet**: Represents animals available for adoption with attributes including ID, name, type (dog/cat), sex, location found, age, weight, breed, size, disability status, and adoption status. Pets can be marked as "disponível" (available) or adopted with associated adopter information.

2. **Pessoa (Person)**: Represents adopters with personal information including name, CPF (Brazilian ID), email, phone, and address. Each person can be associated with multiple pets.

## Data Persistence

**CSV File Storage**: The system uses CSV files as the database layer:
- `petsCadastrados/Pets.csv`: Stores all pet records with 14 fields including adoption status and adopter details (nome_adotante, cpf_adotante, telefone_adotante)
- `adotantesCadastrados/Adotantes.csv`: Stores adopter information with 5 basic fields

**Shared CSV Schema**: All CSV write operations use a shared constant `CAMPOS_PET_CSV` to ensure consistency across registration, editing, deletion, and adoption operations. This guarantees adopter linkage data is preserved.

**Auto-incrementing IDs**: Pet records use a custom ID generation system that creates sequential 5-digit IDs (00001, 00002, etc.) by reading the `id_pet` field using `csv.DictReader` for safe parsing that handles commas in data fields.

**File Structure Management**: The application automatically creates necessary directories and CSV files with headers if they don't exist.

## Business Logic

**Enumerations for Data Validation**: The system uses Python Enums to enforce valid values:
- `TipoAnimal`: Restricts pet types to Cachorro (Dog) or Gato (Cat)
- `SexoAnimal`: Restricts sex to Macho (Male) or Fêmea (Female)

**Menu-Driven Operations**: Seven core operations are supported:
1. Pet registration
2. Pet information updates
3. Pet deletion
4. List all pets
5. Search pets by criteria (age, name, breed, ID, availability)
6. Pet adoption processing
7. System exit

**Adoption Workflow**: When a pet is adopted, the system:
1. Creates or retrieves adopter information and stores it in Adotantes.csv
2. Links the pet record with adopter information by storing nome_adotante, cpf_adotante, and telefone_adotante directly in the pet's CSV record
3. Updates the pet's isAdotado status from "disponível" to "adotado"
4. Preserves this linkage across all subsequent edit and delete operations using the shared CAMPOS_PET_CSV schema

# External Dependencies

## Standard Library Only

The application relies exclusively on Python's standard library:

- **csv**: For reading and writing CSV files (data persistence layer)
- **os**: For file system operations (directory creation, path handling, screen clearing)
- **enum**: For creating enumerated types (data validation)

## File System Requirements

The application expects and creates the following directory structure:

```
/petsCadastrados/     # Pet records storage
  Pets.csv
/adotantesCadastrados/ # Adopter records storage
  Adotantes.csv
/texts/                # Configuration and UI text
  menu.txt
  formulario.txt
/classes/              # Business logic modules
```

## No External Services

The system operates entirely offline with no external API integrations, databases, or third-party services. All data is stored locally in CSV format.