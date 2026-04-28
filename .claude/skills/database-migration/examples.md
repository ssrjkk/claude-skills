# Database Migration Examples

## Create Users Table
```python
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
```

## Add Email Column
```python
def upgrade():
    op.add_column('users', sa.Column('email', sa.String()))
```
