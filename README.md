# Django Web Platform

A full-featured Django web application that combines authentication, personal content, project discovery, and blog publishing in a single, extensible platform.

## Overview

This project is a scalable web platform built with Django and designed around a clear multi-page structure. It includes public-facing pages, authenticated user areas, content management features, and an administrative layer that supports future expansion without requiring a major redesign.

The application is intended to demonstrate practical full-stack web development skills rather than a single isolated feature. It brings together user authentication, database-backed content, search, profile management, and polished frontend styling into one cohesive product.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/matignat/WWW/
   ```

2. Install dependencies and sync the environment:
   ```bash
   uv sync
   ```

3. Apply database migrations:
   ```bash
   uv run python manage.py migrate
   ```

4. Start the development server:
   ```bash
   uv run python manage.py runserver
   ```

5. Open the app in your browser:
   ```text
   http://127.0.0.1:8000/
   ```

## Project Structure

```text
accounts/   # user accounts, authentication, profiles
blog/       # blog posts, comments, blog-related logic
mysite/     # project settings, URLs, core configuration
pages/      # static or general site pages
manage.py   # Django management entry point
uv.lock     # locked project dependencies
```

## Database

The project uses Django migrations to create the database schema.  
Run the following command after cloning the repository:

```bash
uv run python manage.py migrate
```

## Features

### Authentication and Accounts

- User registration and standard login flow.
- GitHub OAuth login for streamlined third-party authentication.
- User profile page available after login.
- Access control for authenticated actions, including creating blog posts.
- Account-oriented structure suitable for future personalization and permission expansion.

### Blog System

- Blog section with posts stored in an SQL-backed database.
- Comment support for post interaction and discussion.
- Post creation restricted to authenticated users.
- Timestamps associated with content to track publishing activity.
- Post detail views with visit counting and per-post display pages.

### Projects Section

- Dedicated projects page for presenting selected work.
- Built-in project search for quick filtering and browsing.
- Structure designed to make adding new entries simple as the portfolio grows.

### Pages and Navigation

- Home page introducing the platform.
- About page with personal information.
- Projects page for portfolio content.
- Blog page for posts and discussions.
- Login page and authenticated profile page.
- Multi-page architecture with clear separation of concerns.

### Administration and Maintainability

- Administrative panels for managing application data and content.
- Modular Django-based architecture that is easy to extend.
- Suitable foundation for distribution, further deployment work, and long-term feature growth.

### Frontend and User Experience

- Custom HTML templates and CSS styling.
- Animated interface elements that improve the overall presentation.
- Professional visual structure across multiple pages and user flows.

## Technology Stack

- **Backend:** Python, Django.
- **Frontend:** HTML, CSS, Django templates.
- **Database:** SQL-based storage for posts, comments, and user-related data.
- **Authentication:** Standard account login plus GitHub OAuth integration.
- **Administration:** Django administrative tooling and custom management workflows.

## Main Capabilities

This application demonstrates the ability to design and implement a real multi-feature web system rather than a basic tutorial project. It covers authentication, route and page organization, template-driven rendering, protected actions, content storage, search functionality, and admin-oriented maintenance in one codebase.

The project shows practical experience with building a service that users can navigate, interact with, and extend over time. It also reflects attention to both backend logic and frontend usability through authentication flows, content management, and polished interface styling.
- `uv.lock` is included to keep dependencies reproducible across environments.
- `uv sync` installs the environment from the lockfile.
- Use `uv run` to execute Django management commands inside the project environment.
