#include "lists.h"
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;
	int count = 0, index = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL || *head == NULL)
		return (NULL);
	new->n = number;
	while (new->n > current->n)
	{
		current = current->next;
		count++;
	}
	current = *head;
	for (index = 0; index < (count - 1); index++)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
