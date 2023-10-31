#include "lists.h"
/**
 * insert_node - insert node to sorted list in approprate index
 * @head: pointer to head
 * @number: number to be set in node
 * Return: address of inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev;

	new = malloc(sizeof(listint_t *));
	if (!head)
	{
		return (NULL);
	}
	new->n = number;
	if (number < (*head)->n)
	{
		new->next = (*head)->next;
		*head = new;
		return (new);
	}
	prev = *head;
	while (prev->next)
	{
		if (number < (prev->next)->n)
		{
			new->next = prev->next;
			prev->next = new;
			return (new);
		}
		prev = prev->next;
	}
	new->next = NULL;
	prev->next = new;
	return (new);
}
